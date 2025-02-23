const redis = require("redis")


const checkAuth = async (args) => {
    const [user, secret] = (args.token || "_:_").split(":");
    const client = await redis.createClient({ url: args.REDIS_URL})
        .on('error', error => console.log('Error during Redis connection'))
        .connect()
    let result = false;
    try {

        const key = await client.get(`${args.REDIS_PREFIX}TOKEN:${user}`);

        result = key === secret;
    } catch (error) {
        console.log(`Redis key error ${error}`);
        result = false;
    };
    return result;
}

exports.auth = async (args) => {
    let result = {
        body:
        {
            output: "Unhauthorized"
        }
    }
    if(await checkAuth(args)) {
        result.body.output = "Authorized"
    }
    return result;
}