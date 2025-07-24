import axios from "axios";

export const getAll = async () => {
  const response = await axios.get("http://localhost:8001/getAll");
  console.log(response);
  if (response.status !== 200) {
    throw new Error("Network response was not ok");
  }
  const data = response.data;
  console.log(data);
  return data;
};
