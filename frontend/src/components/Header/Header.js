import css from "./Header.module.css"
import {Link} from "react-router-dom";
import {UserInfo} from "../UserInfo/UserInfo";
import {useEffect, useState} from "react";

const Header = () => {
    const [trigger, setTrigger] = useState()
    const token = localStorage.getItem('access')
    useEffect(() => {

    }, [trigger, token]);
    return (
        <header className={css.HeaderWrap}>
            <div className={`${css.HeaderBox} wrapper`}>
                <Link className={'my-link'} to={''}>AutoRia Clone</Link>

                <div>
                    <UserInfo setTrigger={setTrigger}/>
                </div>
            </div>
        </header>
    );
};

export {Header};