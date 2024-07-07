import css from "./Advert.module.css";
import {useNavigate} from "react-router-dom";
const Advert = ({advert}) => {
    const {id, name, info, region, car} = advert
    const navigate = useNavigate()
    return (
        <div className={css.advertBox} onClick={()=>navigate(`/details/${id}`)}>
            <div className={css.imageBox}>{car.brand}</div>
            <div>{name}</div>
            <div className={css.info}>
                <h4>{car.price}</h4>
                <div>region: {region}</div>
            </div>
        </div>
    );
};

export {Advert};