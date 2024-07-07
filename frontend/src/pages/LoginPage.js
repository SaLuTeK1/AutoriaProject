import {useForm} from "react-hook-form";
import {authService} from "../services/authService";
import {Link, useNavigate} from "react-router-dom";

const LoginPage = () => {

    const {handleSubmit, register} = useForm();
    const navigate = useNavigate();
    const onSubmit = async (user) => {
        console.log(user)
        await authService.login(user)
        navigate('/home')
    }
    return (

        <div className={'wrapper login-box'}>
            <div>
                <h1>Let`s start!</h1>
                <h2>First - login</h2>
            </div>
            <form onSubmit={handleSubmit(onSubmit)}
                  className={'login-form'}
                  >
                <input type="text" placeholder={'email'} {...register('email')}/>
                <input type="text" placeholder={'password'} {...register('password')}/>
                <button className={'btn log-btn'}>login</button>
                <div style={{display:'flex'}}>
                    <h4>New there? </h4>
                    <Link className={'my-link'} style={{fontSize: "16px"}} to={'/sign_up'}>Sign Up</Link>
                </div>
            </form>
        </div>
    );
};

export {LoginPage};