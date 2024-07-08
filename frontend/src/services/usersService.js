import {apiService} from "./apiService";
import {urls} from "../constants/urls";

const usersService = {
    getProfile:()=>apiService.get(urls.users.profile),

    create:(data)=>apiService.post(urls.users.base,data)
}
export { usersService }