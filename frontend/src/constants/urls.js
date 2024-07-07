const baseURL = '/api'
const socketBaseURL = 'ws://localhost/api'

const urls = {
    users:{
        base:'/users',
        ban:'/ban',
        profile:'/users/profile',
    },
    auth:{
        login:'/auth',
        socket: `/auth/socket`
    },
    cars:{
        base:'/cars',
        brands:'/cars/brands',
        models:(brand)=>`/cars/models?brand=${brand}`,
        bodies:'/cars/bodies',
    },
    advert:{
        base:'/advert',
        byId:(id)=>`/advert/${id}`,
        region:'/advert/regions'
    }
}

export {urls,baseURL,socketBaseURL}