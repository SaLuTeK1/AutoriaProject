import {SearchForm} from "../components/Forms/SearchForm/SearchForm";
import {useEffect, useState} from "react";
import {advertService} from "../services/advertService";
import {Adverts} from "../components/AdvertsContainer/Adverts/Adverts";
import {socketService} from "../services/socketService";
import {client} from "websocket";
import {useNavigate} from "react-router-dom";

const HomePage = () => {
    const [adverts, setAdverts] = useState([])
    const [trigger, setTrigger] = useState()

    useEffect(() => {
        advertService.getAll().then(({data}) => setAdverts(data.data))
    }, [trigger]);

    useEffect(() => {
        socketInit()
    }, []);

    const socketInit = async () => {
        const {adverts} = await socketService()
        const client = await adverts()

        client.onopen = () => {
            console.log('connected');
            client.send(JSON.stringify({
                action: 'sub_to_advers_activity',
                req_id: new Date().getTime()
            }))
        }
        client.onmessage = ({data}) => {
            console.log(data.toString())
            setTrigger(prev => !prev)
        }
    }


    console.log(adverts)
    const navigate = useNavigate()
    return (
        <div className="wrapper">
            <div style={{display: "flex", justifyContent: "space-between"}}>
                <SearchForm/>
                <button className={'create-btn'} onClick={() => navigate('/create')}>SOLD YOUR CAR</button>
            </div>
            <Adverts adverts={adverts}/>
        </div>
    );
};

export {HomePage};