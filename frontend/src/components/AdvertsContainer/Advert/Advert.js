import css from "./Advert.module.css";
const Advert = ({advert}) => {
    const {id, name, info, region, car} = advert

    return (
        <div className={css.advertBox}>
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