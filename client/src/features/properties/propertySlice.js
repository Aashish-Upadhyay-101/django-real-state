import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import { errorMessage } from "../../helpers/errorMessage";
import propertyAPIService from "./propertyAPIService";

const initialState = {
  properties: [],
  property: {},
  isError: false,
  isLoading: false,
  isSuccess: false,
  message: "",
};

// get all properties
export const getProperties = createAsyncThunk(
  "properties/getAll",
  async (_, thunkAPI) => {
    try {
      return await propertyAPIService.getProperties();
    } catch (error) {
      const message = errorMessage(error);
      return thunkAPI.rejectWithValue(message);
    }
  }
);

export const propertySlice = createSlice({
  name: "Properties",
  initialState,

  reducers: {
    reset: (state) => initialState,
  },
  extraReducers: (builder) => {
    builder
      .addCase(getProperties.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(getProperties.fulfilled, (state, action) => {
        state.isLoading = false;
        state.isSuccess = true;
        state.properties = action.payload.results;
      })
      .addCase(getProperties.rejected, (state, action) => {
        state.isLoading = false;
        state.isError = true;
        state.message = action.payload;
      });
  },
});

export const { reset } = propertySlice.actions;
export default propertySlice.reducer;
