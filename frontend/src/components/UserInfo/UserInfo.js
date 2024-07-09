import {useContext, useEffect, useState} from "react";
import {usersService} from "../../services/usersService";
import {Link, useNavigate} from "react-router-dom";
import {MyContext} from "../../hoc/ContextProvider";

const UserInfo = () => {
    const {trigger, toggleTrigger} = useContext(MyContext);


    const [profile, setProfile] = useState(null)
    const token = localStorage.getItem('access')


    useEffect(() => {
        if (token) {
            const tokenParts = token.split('.');
            const decodedPayload = JSON.parse(atob(tokenParts[1]));
            setProfile(decodedPayload.name);
        }
    }, [trigger]);

    const navigate = useNavigate();

    const logOut = () => {
        localStorage.removeItem('access');
        toggleTrigger()
        setProfile(null)
    }

    return (
        <div>
            {token ?
                <div style={{display: 'flex'}}>
                    <div>
                        {profile}
                    </div>
                    <button className={`log-btn btn`} onClick={() => logOut()}>Log Out</button>
                </div>
                :
                <div>
                    <button className={`log-btn btn`} onClick={() => navigate('/login')}>Log In</button>
                </div>}
        </div>

    );
};

export {UserInfo};