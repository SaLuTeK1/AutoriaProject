const AdvertInfo = ({advert}) => {
    const {name, info, region, car, views, avg_price_region} = advert

    return (
        <div>
            <div>
                <h2>
                    {name}
                </h2>
            </div>
            <div>
                <div className="info">
                    <h2>{car.brand}</h2>
                    <h2>{region}</h2>
                    <h2>{car.model}</h2>
                </div>
                <div>
                    {views} and
                    {avg_price_region}
                </div>
            </div>
        </div>
    )
        ;
};

export {AdvertInfo};