"use client";

import { useState } from "react";
import api from "./api";
import toast from "react-hot-toast";
import SearchTerm from "./Components/SearchTerm";
import UploadDocument from "./Components/UploadDocument";

export default function Home() {

  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [searchTerm, setSearchTerm] = useState("");
  const [results, setResults] = useState([]);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const submitFile = async () => {
    if (!file) {
      toast.error("Please select a file");
      return;
    }

    try{
      setLoading(true);

      const formData = new FormData();
      formData.append("file", file);

      const response = await api.post("/ingest", formData);
      toast.success(response.data.message);
      setFile(null);
    } catch (error) {
      toast.error(error.response.data.detail || error.message || "An error occurred");
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = async () => {
    if (!searchTerm) {
      toast.error("Please enter a search term");
      return;
    }

    try{
      const response = await api.get("/search", { params: { query: searchTerm } });
      setResults(response.data.results);
    } catch (error) {
      toast.error(error.response.data.detail || error.message || "An error occurred");
    }
  };

  return (
    <div className="w-screen min-h-screen bg-gray-50 flex flex-col justify-center items-center">
      <div className="w-full p-8 bg-white shadow-lg rounded-none">
        <UploadDocument
          handleFileChange={handleFileChange}
          submitFile={submitFile}
          loading={loading}
        />
        <SearchTerm
          searchTerm={searchTerm}
          setSearchTerm={setSearchTerm}
          handleSearch={handleSearch}
          results={results}
        />
      </div>
    </div>
  );
}