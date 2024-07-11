import {Link, useParams} from "react-router-dom";
import {useEffect} from "react";
import {authService} from "../services/authService";

const ActivateAccountPage = () => {
    const {token} = useParams();

    useEffect(() => {
        authService.activateAccount(token)
    })

    return (
        <div className={'wrapper'}>
            <h1>
                You have activate account successfully
            </h1>
            <Link to="/login">LogIn</Link>
        </div>
    );
};

export {ActivateAccountPage};