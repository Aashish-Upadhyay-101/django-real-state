import { configureStore } from "@reduxjs/toolkit";
import {} from "../features/properties/propertySlice";

const store = configureStore({
  reducer: {
    properties: propertyReducer,
    auth: authReducer,
  },
});
