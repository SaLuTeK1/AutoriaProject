import {apiService} from "./apiService";
import {urls} from "../constants/urls";

const carsService = {
    getBrands(){
        return apiService.get(urls.cars.brands)
    },
    getModels(brand){
        return apiService.get(urls.cars.models(brand))
    },
    getBodies(){
        return apiService.get(urls.cars.bodies)
    }
}

export {carsService}