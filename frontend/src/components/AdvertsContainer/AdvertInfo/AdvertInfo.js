import {useEffect, useState} from "react";

const AdvertInfo = ({advert}) => {
    const {name, info, region, car, views, avg_price_region} = advert

    const [isPremium, setIsPremium] = useState(false)
    const token = localStorage.getItem('access');


    useEffect(() => {
        if (token) {
            const tokenParts = token.split('.');
            const decodedPayload = JSON.parse(atob(tokenParts[1]));
            setIsPremium(decodedPayload.is_premium);
        }
    }, []);

    console.log('Is Premium:', isPremium);


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
                {
                    isPremium ? <div>
                        {views} and
                        {avg_price_region}
                    </div> : <div></div>
                }

            </div>
        </div>
    )
        ;
};

export {AdvertInfo};