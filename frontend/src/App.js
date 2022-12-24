import { useState, useEffect } from "react";
import NotesList from "./components/NotesList";
import Search from "./components/Search";
import Header from "./components/Header";

const App = () => {
  const [notes, setNotes] = useState([]);
  const [searchText, setSearchText] = useState("");
  const [darkMode, setDarkMode] = useState(false);

  const fetchNotes = async () => {
    const response = await fetch("http://localhost:8000/api/v1/notes");
    const data = await response.json();
    if (!response.ok) {
      throw Error(data.detail);
    }
    setNotes(data);
  };

  const sendNote = async (newNote) => {
    const response = await fetch("http://localhost:8000/api/v1/notes", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ newNote }),
    });

    const data = await response.json();
    if (!response.ok) {
      throw Error(data.detail);
    }
  };

  const removeNote = async (id) => {
    const response = await fetch(`http://localhost:8000/api/v1/notes/${id}`, {
      method: "DELETE",
    });
    const data = await response.json();
    if (!response.ok) {
      throw Error(data.detail);
    }
  };

  useEffect(() => {
    try {
      fetchNotes();
    } catch (error) {
      console.log(error);
    }
  }, []);

  const addNote = async (text) => {
    const date = new Date();
    const newNote = {
      text: text,
      date: date.toLocaleDateString(),
    };

    try {
      sendNote(newNote);
      const newNotes = [...notes, newNote];
      setNotes(newNotes);
    } catch (error) {
      console.log(error);
    }
  };

  const deleteNote = async (id) => {
    try {
      removeNote(id);
      const newNotes = notes.filter((note) => note.id !== id);
      setNotes(newNotes);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className={`${darkMode && "dark-mode"}`}>
      <div className="container">
        <Header handleToggleDarkMode={setDarkMode} />
        <Search handleSearchNote={setSearchText} />
        <NotesList
          notes={notes.filter((note) =>
            note.text.toLowerCase().includes(searchText)
          )}
          handleAddNote={addNote}
          handleDeleteNote={deleteNote}
        />
      </div>
    </div>
  );
};

export default App;
