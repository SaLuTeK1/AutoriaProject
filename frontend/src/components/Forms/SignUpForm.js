import React from 'react';
import {Link, useNavigate} from "react-router-dom";
import {useForm} from "react-hook-form";
import {usersService} from "../../services/usersService";

const SignUpForm = () => {
    const {register,reset, handleSubmit} = useForm()
    const navigate = useNavigate()
    const onSubmit = (user) =>{
        console.log(user)
        usersService.create(user)
        // navigate('/login')
        // reset()
    }
    return (
        <form onSubmit={handleSubmit(onSubmit)}
              className={'login-form'}
              style={{
                  margin:"100px auto"
              }}
        >
            <input type="email" placeholder={'Enter your email'} {...register('email')}/>
            <input type="text" placeholder={'Enter your password'} {...register('password')}/>
            <input type="text" placeholder={'Enter your name'} {...register('profile.name')}/>
            <input type="text" placeholder={'Enter your surname'} {...register('profile.surname')}/>
            <input type="number" placeholder={'Enter your age'} {...register('profile.age')}/>
            <input type="text" placeholder={'Enter your mobile nubmer'} {...register('profile.phone')}/>

            <button className={'btn log-btn'}>Sign Up</button>
        </form>
    );
};

export {SignUpForm};