import {NotFoundCar} from "../components/Forms/NotFoundCar/NotFoundCar";

const NotFoundCarPage = () => {
    return (
        <div className={'wrapper'} style={{display: 'flex', margin: '0 auto', paddingTop:"100px"}}>
            <div style={{ marginRight: '150px'}}>
                <h2>Oh bro, I wish it`ll help</h2>
            </div>
            <NotFoundCar/>
        </div>
    );
};

export {NotFoundCarPage};