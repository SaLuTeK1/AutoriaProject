const baseURL = '/api/'

const urls = {
    users:{
        base:'users',
        ban:'ban'
    },
    auth:{
        login:'auth',

    },
    cars:{
        base:'cars'
    },
    advert:{
        base:'advert',
        byId:(id)=>`advert/${id}`
    }
}

export {urls,baseURL}