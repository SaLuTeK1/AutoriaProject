import {apiService} from "./apiService";
import {urls} from "../constants/urls";

const usersService = {
    getProfile:()=>apiService.get(urls.users.profile),
}
export { usersService }