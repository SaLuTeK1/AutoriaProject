import {useEffect, useState} from "react";
import {usersService} from "../../services/usersService";
import {Link, useNavigate} from "react-router-dom";

const UserInfo = ({setTrigger}) => {
    const [profile, setProfile] = useState(null)
    const token = localStorage.getItem('access')

    useEffect(() => {
        if (token) {
            usersService.getProfile().then(({data}) => setProfile(data))
        }
    }, []);

    const navigate = useNavigate();

    const logOut = () => {
        localStorage.removeItem('access');
        setTrigger(prev => !prev)
        setProfile(null)
    }

    return (
        <div>
            {profile ?
                <div style={{display: 'flex'}}>
                    <div>
                        {profile.name}
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