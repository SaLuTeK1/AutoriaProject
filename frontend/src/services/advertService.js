import {urls} from "../constants/urls";
import {apiService} from "./apiService";

const advertService = {
    getAll: (filter) => {
    let query = '';

    if (filter && Object.keys(filter).length > 0) {
      query = '?' + new URLSearchParams(filter).toString();
    }

    return apiService.get(`${urls.advert.base}${query}`);
  },
    getById: (id) => apiService.get(urls.advert.byId(id)),
    create(data) {
        return apiService.post(urls.advert.create, data)
    },
    getRegions:() => apiService.get(urls.advert.region),
}

export {advertService}