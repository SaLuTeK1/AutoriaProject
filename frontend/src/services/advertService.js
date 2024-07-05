import {urls} from "../constants/urls";
import {apiService} from "./apiService";

const advertService = {
    getAll:()=>apiService.get(urls.advert.base,),
    getById:(id)=>apiService.get(urls.advert.byId(id)),
}

export {advertService}