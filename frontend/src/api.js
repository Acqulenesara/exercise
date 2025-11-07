import axios from "axios";
const API_BASE = "http://localhost:8000";

export const savePostureData = async (payload) => {
  try {
    const res = await axios.post(`${API_BASE}/posture`, payload);
    return res.data;
  } catch (err) {
    console.error("Error saving posture:", err);
  }
};
