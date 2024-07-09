import css from "./Header.module.css"
import {Link} from "react-router-dom";
import {UserInfo} from "../UserInfo/UserInfo";

const Header = () => {

    return (
        <header className={css.HeaderWrap}>
            <div className={`${css.HeaderBox} wrapper`}>
                <Link className={'my-link'} to={''}>AutoRia Clone</Link>
                <div>
                    <UserInfo />
                </div>
            </div>
        </header>
    );
};

export {Header};