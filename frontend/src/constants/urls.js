const baseURL = '/api'
const socketBaseURL = 'ws://Autoria-clone-project-env.eba-ws6pm7q5.us-east-1.elasticbeanstalk.com/api'
const images = 'Autoria-clone-project-env.eba-ws6pm7q5.us-east-1.elasticbeanstalk.com/media/'
const urls = {
    users:{
        base:'/users',
        ban:'/users/ban',
        profile:'/users/profile',
        notify:'/users/notify',
    },
    auth:{
        login:'/auth',
        socket: `/auth/socket`,
        activate:(token)=>`/auth/activate/${token}`
    },
    cars:{
        base:'/cars',
        brands:'/cars/brands',
        models:(brand)=>`/cars/models?brand=${brand}`,
        bodies:'/cars/bodies',
    },
    advert:{
        base:'/advert',
        create:'/advert/create',
        byId:(id)=>`/advert/${id}`,
        region:'/advert/regions',
    }
}

export {urls,baseURL,socketBaseURL, images}