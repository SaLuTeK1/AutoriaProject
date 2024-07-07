import {Advert} from "../Advert/Advert";
import css from './Adverts.module.css'
const Adverts = ({adverts}) => {


    return (
        <div className={css.AdvertsBox}>
            {adverts.map(advert=><Advert key={advert.id} advert={advert}/>)}
        </div>
    );
};

export {Adverts};