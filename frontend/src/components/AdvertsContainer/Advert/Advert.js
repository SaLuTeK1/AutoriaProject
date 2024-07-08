import css from "./Advert.module.css";
import {useNavigate} from "react-router-dom";
import {images} from "../../../constants/urls"
const Advert = ({advert}) => {
    const {id, name, info, region, car, car_photo} = advert
    const navigate = useNavigate()
    return (
        <div className={css.advertBox} onClick={()=>navigate(`/details/${id}`)}>
            {car_photo ?
                <img src={`${images}/${car_photo}`} alt={name}/>
                :
               <div className={css.imageBox}></div>
            }

            <div>{name}</div>
            <div className={css.info}>
                <h4>{car.price} {car.currency}</h4>
                <div> {region}</div>
            </div>
        </div>
    );
};

export {Advert};