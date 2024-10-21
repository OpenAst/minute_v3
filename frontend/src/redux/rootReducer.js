import { combineReducers } from "@reduxjs/toolkit";
import authReducer from '../features/auth/authSlice';

const rootReducer = combineReducers({
    auth: authReducer,
    // Add other reducers
});

export default rootReducer;