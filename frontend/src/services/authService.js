import {apiService} from "./apiService";
import {urls} from "../constants/urls";

const authService = {
    async login(user){
        const {data:{access}} = await apiService.post(urls.auth.login)
        localStorage.setItem('access', access)
    }
}

export {
    authService
}