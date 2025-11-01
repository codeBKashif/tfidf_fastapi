export default function UploadDocument({ handleFileChange, submitFile, loading }) {
    return (
      <div className="flex items-center justify-center w-full gap-4 mb-8">
        <input
          accept=".txt"
          type="file"
          name="file"
          onChange={handleFileChange}
          className="flex-grow h-12 text-sm text-gray-700 border border-gray-300 rounded-lg cursor-pointer focus:outline-none 
                    file:mr-4 file:h-12 file:px-4 file:rounded-md file:border-0 
                    file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 
                    hover:file:bg-blue-100"
        />
        <button
          onClick={submitFile}
          disabled={loading}
          className={`h-12 px-6 font-medium rounded-lg transition ${
            loading
              ? 'bg-gray-400 text-gray-100 cursor-not-allowed'
              : 'bg-blue-600 text-white hover:bg-blue-700'
          }`}
        >
          {loading ? 'Uploading...' : 'Upload'}
        </button>
      </div>
    );
  }
  