import {useEffect, useState} from "react";
import {usersService} from "../../services/usersService";

const UserInfo = () => {
    const [profile, setProfile] = useState({name: '', email: ''})
    const token = localStorage.getItem('access')
    useEffect(() => {
        usersService.getProfile().then(({data}) => setProfile(data))
    }, []);
    return (
        <div>
            {profile ?
                <div>
                {profile.name}
                {profile.email}
            </div> : <div></div>}
        </div>

    );
};

export {UserInfo};