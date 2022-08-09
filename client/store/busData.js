export const state = () => ({
  item: [],
  openDelete: false,
});

export const mutations = {
  setData(state, item) {
    state.item = item;
    state.openDelete = true;
  },
  setClose(state, item, status) {
    state.item = item;
    state.openDelete = status;
  },
};
