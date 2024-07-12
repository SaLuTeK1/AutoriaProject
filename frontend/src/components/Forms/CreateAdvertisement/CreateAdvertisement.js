import {useForm} from "react-hook-form";
import {useEffect, useState} from "react";
import {carsService} from "../../../services/carsService";
import {advertService} from "../../../services/advertService";
import {CustomDropdown} from "../CustomDropdown/CustomDropdown";
import {CreateCarPage} from "../../../pages/CreateCarPage";
import {Link} from "react-router-dom";
import {joiResolver} from "@hookform/resolvers/joi";
import {formCreateValidators} from "../../../validators/formValidator";

const currency = ['USD', 'UAH', 'EUR'];

const CreateAdvertisement = () => {
    const {handleSubmit, reset, register, watch, setValue,formState:{isValid,errors}} = useForm({
        mode: 'all',
        resolver: joiResolver(formCreateValidators)
    });

    const [brands, setBrands] = useState([])
    const [models, setModels] = useState([])
    const [regions, setRegions] = useState([])
    const [bodies, setBodies] = useState([])

    const selectedBrand = watch('car.brand');
    console.log()
    useEffect(() => {
        carsService.getBrands().then(({data}) => setBrands(data))
        advertService.getRegions().then(({data}) => setRegions(data))
        carsService.getBodies().then(({data}) => setBodies(data))
    }, []);

    useEffect(() => {
        if (selectedBrand) {
            carsService.getModels(selectedBrand).then(({data}) => setModels(data));

        } else {
            setModels([]);
        }
    }, [selectedBrand]);

    const save = (data) => {
        advertService.create(data)
        reset();
    }


    console.log(isValid)
    return (
        <form onSubmit={handleSubmit(save)} className="create-advertisement-form wrapper">
            <div className="form-group">
                <input
                    type="text"
                    name="name"
                    placeholder="Enter title"
                    className="form-control"
                    {...register('name')}
                />
                {errors.name &&<div>{errors.name.message}</div>}
            </div>

            <div className="form-group">
                <CustomDropdown
                    options={regions}
                    name="region"
                    placeholder="Region"
                    setValue={setValue}
                    watch={watch}
                />
                {errors.region &&<div>{errors.region.message}</div>}
            </div>
            <div className="form-group">
                <CustomDropdown
                    options={brands}
                    name="car.brand"
                    placeholder="Brand"
                    setValue={setValue}
                    watch={watch}
                />
                {errors.brand &&<div>{errors.brand.message}</div>}
            </div>
            <div className="form-group">
                <CustomDropdown
                    options={models}
                    name="car.model"
                    placeholder="Model"
                    setValue={setValue}
                    watch={watch}
                    disabled={!selectedBrand}
                />
                 {errors.model &&<div>{errors.model.message}</div>}
            </div>

            <div className="form-group">
                <input
                    type="number"
                    name="car.year"
                    placeholder="Enter year"
                    className="form-control"
                    {...register('car.year', {valueAsNumber: true})}
                />
                {errors.year &&<div>{errors.year.message}</div>}
            </div>

            <div className="form-group">

                <input
                    type="number"
                    step="0.1"
                    name="car.engine"
                    placeholder="Enter engine capacity"
                    className="form-control"
                    {...register('car.engine', {valueAsNumber: true})}
                />
                {errors.engine &&<div>{errors.engine.message}</div>}
            </div>
            {/*<div className="form-group">*/}

            {/*    <input*/}
            {/*        type="text"*/}
            {/*        name="car.fuel"*/}
            {/*        placeholder="Enter fuel type"*/}
            {/*        className="form-control"*/}
            {/*        {...register('car.fuel', { valueAsNumber: true })}*/}
            {/*    />*/}
            {/*</div>*/}
            <div className="form-group">
                <CustomDropdown
                    options={bodies}
                    name="car.body_type"
                    placeholder="Enter body type"
                    setValue={setValue}
                    watch={watch}
                />
                {errors.body_type &&<div>{errors.body_type.message}</div>}
            </div>
            <div className="form-group">
                <input
                    type="text"
                    name="car.drive"
                    placeholder="Enter drive type"
                    className="form-control"
                    {...register('car.drive')}
                />
                {errors.drive &&<div>{errors.drive.message}</div>}
            </div>
            {/*<div className="form-group">*/}
            {/*    <input*/}
            {/*        type="text"*/}
            {/*        name="car.gearbox"*/}
            {/*        placeholder="Enter gearbox type"*/}
            {/*        className="form-control"*/}
            {/*        {...register('car.gearbox')}*/}
            {/*    />*/}
            {/*</div>*/}
            <div className="form-group">
                <input
                    type="number"
                    name="car.capacity"
                    placeholder="Enter capacity"
                    className="form-control"
                    {...register('car.capacity', {valueAsNumber: true})}
                />
                {errors.capacity &&<div>{errors.capacity.message}</div>}
            </div>
            <div className="form-group">
                <input
                    type="number"
                    name="car.mileage"
                    placeholder="Enter mileage"
                    className="form-control"
                    {...register('car.mileage', {valueAsNumber: true})}
                />
                {errors.mileage &&<div>{errors.mileage.message}</div>}
            </div>

            <div className="form-group">
                <input
                    type="number"
                    name="car.price"
                    placeholder="Enter price"
                    className="form-control"
                    {...register('car.price', {valueAsNumber: true})}
                />
                {errors.price &&<div>{errors.price.message}</div>}
            </div>
            <div className="form-group">
                <input
                    list='currency'
                    name="car.currency"
                    placeholder="Enter currency"
                    className="form-control"
                    {...register('car.currency')}
                />
                <datalist id="currency">
                    {currency.map((cur, index) => (
                        <option key={index} value={cur}/>
                    ))}
                </datalist>
                {errors.currency &&<div>{errors.currency.message}</div>}
            </div>
            <div className="form-group">
                <textarea
                    style={{resize: "none"}}
                    name="info"
                    placeholder="Enter information"
                    className="form-control"
                    {...register('info')}
                />
                {errors.info &&<div>{errors.info.message}</div>}
            </div>
            {/*<div className="form-group">*/}
            {/*    <input type={"file"}*/}
            {/*           name={'car_photo'}*/}
            {/*           placeholder={"Upload car photo"}*/}
            {/*           className="form-control"*/}
            {/*           onChange={handleChange}*/}
            {/*           {...register('car_photo', {required: true})}*/}

            {/*    />*/}
            {/*</div>*/}


            <div className="form-group">
                <div>
                    <h5>Not found your car?</h5>
                    <Link className={'my-link-not'} to={'/notify'}>Notify our managers!</Link>
                </div>
                <button type="submit" disabled={!isValid} className={'btn log-btn'}>Save</button>
            </div>
        </form>
    );
};

export {CreateAdvertisement};
