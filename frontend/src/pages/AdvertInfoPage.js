import {useEffect, useState} from "react";
import {advertService} from "../services/advertService";
import {useLoaderData} from "react-router-dom";
import {AdvertInfo} from "../components/AdvertsContainer/AdvertInfo/AdvertInfo";


const AdvertInfoPage = () => {
    const [advert, setAdvert] = useState(null)
    const {data} = useLoaderData()
    useEffect(() => {
        setAdvert(data)
        console.log(data)
    }, []);
    return (
        <div>
            {advert&&<AdvertInfo advert={advert}/>}
        </div>
    );
};

export {AdvertInfoPage};