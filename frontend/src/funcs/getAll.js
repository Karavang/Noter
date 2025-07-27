export const getAll = async () => {
  const response = await fetch("http://localhost:8001/getAll");
  console.log(response);
  if (response.status !== 200) {
    throw new Error("Network response was not ok");
  }
  const data = await response.json();

  return data;
};
