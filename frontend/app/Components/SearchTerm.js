
export default function SearchTerm({ searchTerm, setSearchTerm, handleSearch, results }) {
    return (
      <div className="pt-4 border-t border-gray-200">
        <h1 className="text-3xl font-bold text-center text-gray-800 mb-6">
          Document Search
        </h1>
  
        <div className="flex gap-4 mb-6 w-full">
          <input
            type="text"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="Enter search term..."
            className="flex-grow h-12 px-4 border border-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            onClick={handleSearch}
            className="h-12 px-5 bg-blue-600 text-white font-medium rounded-lg hover:bg-blue-700 transition"
          >
            Search
          </button>
        </div>
  
        <ul className="divide-y divide-gray-200 bg-gray-50 rounded-lg p-4 w-full">
          {results.length > 0 ? (
            results.map((result) => (
              <li
                key={result.document}
                className="py-2 flex justify-between text-gray-700"
              >
                <span className="font-medium">{result.document}</span>
                <span className="text-sm text-gray-500">
                  {result.score.toFixed(3)}
                </span>
              </li>
            ))
          ) : (
            <li className="text-center text-gray-400 py-4">No results found</li>
          )}
        </ul>
      </div>
    );
  }
  