import {useForm} from "react-hook-form";
import {usersService} from "../../../services/usersService";

const NotFoundCar = () => {
    const {register,handleSubmit,reset} = useForm()

    const notify = (data) =>{
        usersService.notify(data)
        reset()
    }
    return (
        <form onSubmit={handleSubmit(notify)}>
            <input  type="text" name="notify" placeholder="What car you didn`t find?" {...register('message')}/>
            <button type="submit" className={'btn log-btn'}>Notify</button>
        </form>
    );
};

export {NotFoundCar};