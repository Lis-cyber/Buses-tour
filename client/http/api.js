import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
import moment from "moment";

export const getTimes = () => {
  const hours = Array.from({ length: 24 }, (_, hour) =>
    moment({
      hour: Math.floor(hour),
      minutes: 0,
    }).format("hh:mm a")
  );

  let schedules = []
  function pairwise(arr, func) {
    for (var i = 0; i < arr.length - 1; i++) {
      func(arr[i], arr[i + 1]);
    }
  }
  pairwise(hours, function (current, next) {
    schedules.push(current+" a "+next)
  });

  return schedules;
};

export const service = {
  init() {
    Vue.use(VueAxios, axios);
    Vue.axios.defaults.baseURL = process.env.BASE_URL;
  },
  setHeader() {
    Vue.axios.defaults.headers.common["Content-Type"] = "application/json";
  },
};

const response = {
  data: null,
  error: null,
};

export const getAllItems = async (path) => {
  try {
    const res = await Vue.axios.get(`${path}`);
    response.data = res.data;
    response.error = null;
  } catch (error) {
    response.error = error.message;
    response.data = null;
  }
  return response;
};

export const getItem = async (path, id = null) => {
  try {
    const res = await Vue.axios.get(`${path}/${id}`);
    response.data = res.data;
    response.error = null;
  } catch (error) {
    response.error = error.message;
    response.data = null;
  }
  return response;
};

export const postItem = async (path, data) => {
  try { 
    const res = await Vue.axios.post(`${path}/`, data);
    response.data = res.data;
    response.error = null;
  } catch (error) {
    response.error = error.message;
    response.data = null;
  }
  return response;
};

export const putItem = async (path, id, data) => {
  try {
    const res = await Vue.axios.put(`${path}/${id}/`, data);
    response.data = res.data;
    response.error = null;
  } catch (error) {
    response.error = error.message;
    response.data = null;
  }
  return response;
};

export const deleteItem = async (path, id) => {
  try {
    await Vue.axios.delete(`${path}/${id}`);
    response.error = null;
  } catch (error) {
    response.error = error.message;
  }
  return response;
};
