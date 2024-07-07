import {useForm} from "react-hook-form";
import {useEffect, useState} from "react";
import {carsService} from "../../../services/carsService";
import {advertService} from "../../../services/advertService";
import {CustomDropdown} from "../CustomDropdown/CustomDropdown";

const currency = ['USD', 'UAH', 'EUR'];

const CreateAdvertisement = () => {
    const {handleSubmit, reset, register, watch, setValue} = useForm();

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
    const save = (advert) => {
        advertService.create(advert)
        console.log(advert)
        // reset();
    }

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
            </div>

            <div className="form-group">
                <CustomDropdown
                    options={regions}
                    name="region"
                    placeholder="Region"
                    setValue={setValue}
                    watch={watch}
                />
            </div>
            <div className="form-group">
                <CustomDropdown
                    options={brands}
                    name="car.brand"
                    placeholder="Brand"
                    setValue={setValue}
                    watch={watch}
                />

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
            </div>

            <div className="form-group">
                <input
                    type="number"
                    name="car.year"
                    placeholder="Enter year"
                    className="form-control"
                    {...register('car.year', { valueAsNumber: true })}
                />
            </div>

            <div className="form-group">

                <input
                    type="number"
                    step="0.1"
                    name="car.engine"
                    placeholder="Enter engine capacity"
                    className="form-control"
                    {...register('car.engine', { valueAsNumber: true })}
                />
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
            </div>
            <div className="form-group">
                <input
                    type="text"
                    name="car.drive"
                    placeholder="Enter drive type"
                    className="form-control"
                    {...register('car.drive')}
                />
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
                    {...register('car.capacity', { valueAsNumber: true })}
                />
            </div>
            <div className="form-group">
                <input
                    type="number"
                    name="car.mileage"
                    placeholder="Enter mileage"
                    className="form-control"
                    {...register('car.mileage', { valueAsNumber: true })}
                />
            </div>
            <div className="form-group">
                <input
                    type="number"
                    name="car.price"
                    placeholder="Enter price"
                    className="form-control"
                    {...register('car.price', { valueAsNumber: true })}
                />
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
            </div>
            <div className="form-group">
                <textarea
                    name="info"
                    placeholder="Enter information"
                    className="form-control"
                    {...register('info')}
                />
            </div>
            <button type="submit">Save</button>
        </form>
    );
};

export {CreateAdvertisement};
