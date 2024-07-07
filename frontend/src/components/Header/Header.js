import css from "./Header.module.css"
import {Link} from "react-router-dom";
import {UserInfo} from "../UserInfo/UserInfo";

const Header = () => {
    return (
        <header className={css.HeaderWrap}>
            <div className={`${css.HeaderBox} wrapper`}>
                <div>
                    <h2>Auto</h2>
                    <h2></h2>
                    <h2></h2>
                </div>
                <div>
                    <UserInfo/>
                </div>
            </div>
        </header>
    );
};

export {Header};