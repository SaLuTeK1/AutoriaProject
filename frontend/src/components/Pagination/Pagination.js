import {prev, next} from "../../utils/navigationFunctions";

const Pagination = ({setQuery, totalPages, page}) => {
    return (
        <div>
            <div className={'button-box'}>
                <button className={` my-button`} disabled={page === '1'}
                        onClick={() => prev(setQuery)}>Back
                </button>
                <button className={` my-button`}>{page}</button>
                <button className={` my-button`} disabled={page === `${totalPages}`}
                        onClick={() => next(setQuery)}>Forward
                </button>
            </div>
        </div>
    );
};

export {Pagination};