import {useEffect, useState} from "react";
import axios from "axios";
import {advertService} from "./services/advertService";

const App = () => {
    const [cars, setCars] = useState([])
    useEffect(() => {
        advertService.getAll().then(({data})=>setCars(data))
    }, []);

    console.log(cars)
  return (
      <div>
          {cars.map(car=><div key={car.id}>{JSON.stringify(car)}</div>)}
      </div>
  );
};

export {App};
