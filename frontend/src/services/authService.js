import {apiService} from "./apiService";
import {urls} from "../constants/urls";

const authService = {
    async login(user){
        const {data:{access}} = await apiService.post(urls.auth.login, user)
        localStorage.setItem('access', access)
    },
    getSoketToken() {
        return apiService.get(urls.auth.socket)
    },
    activateAccount(token){
        return apiService.post(urls.auth.activate,token)
    }

}

export {
    authService
}