import { configureStore } from "@reduxjs/toolkit";
import propertyReducer from "../features/properties/propertySlice";
import authReducer from "..features/auth/authSlice";

const store = configureStore({
  reducer: {
    properties: propertyReducer,
    auth: authReducer,
  },
});
