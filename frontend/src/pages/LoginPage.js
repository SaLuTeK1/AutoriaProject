import {useForm} from "react-hook-form";
import {authService} from "../services/authService";
import {Link, useNavigate} from "react-router-dom";

const LoginPage = () => {

    const {handleSubmit, register} = useForm();
    const navigate = useNavigate();
    const onSubmit = async (user) => {
        await authService.login(user)
        navigate('/home')
    }
    return (

        <div>
            <form onSubmit={handleSubmit(onSubmit)}>
                <input type="text" placeholder={'email'} {...register('email')}/>
                <input type="text" placeholder={'password'} {...register('password')}/>
                <button>login</button>
                <Link to={'/sign_up'}>Sign Up</Link>
            </form>
        </div>
    );
};

export {LoginPage};