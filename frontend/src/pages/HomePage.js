import {SearchForm} from "../components/Forms/SearchForm/SearchForm";
import {useEffect, useState} from "react";
import {advertService} from "../services/advertService";
import {Adverts} from "../components/AdvertsContainer/Adverts/Adverts";
import {socketService} from "../services/socketService";

import {useLocation, useNavigate, useSearchParams} from "react-router-dom";
import {Pagination} from "../components/Pagination/Pagination";

const HomePage = () => {
    const [adverts, setAdverts] = useState([])
    const [trigger, setTrigger] = useState()

    const [totalPages, setTotalPages] = useState()

    const location = useLocation();

    const [query, setQuery] = useSearchParams({page: '1'});
    const page = query.get('page')
    const token = localStorage.getItem('access')
    useEffect(() => {
        advertService.getAll(location.search).then(({data}) => {
            setAdverts(data.data)
            setTotalPages(data.total_pages)
            }
        )
    }, [trigger, location]);

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

    const create = ()=>{
        if(token){
            navigate('/create')
        }else {
            navigate('/login')
        }

    }
    console.log(adverts)
    const navigate = useNavigate()
    return (
        <div className="wrapper">
            <div style={{display: "flex", justifyContent: "space-between", margin: '40px 0'}}>
                <SearchForm/>
                <button className={'create-btn'} onClick={() => create()}>SOLD YOUR CAR</button>
            </div>
            <Adverts adverts={adverts} />
            <Pagination totalPages={totalPages} setQuery={setQuery} page={page}/>
        </div>
    );
};

export {HomePage};