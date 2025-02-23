//--kind nodejs:default
//--web true
//--param REDIS_URL $REDIS_URL
//--param REDIS_PREFIX $REDIS_PREFIX

const {auth} = require('./auth')

async function main (args) {
    return await auth(args)

}


module.exports = main