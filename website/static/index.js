function deleteNote(noteId) {
    fetch('/delete-note', { // delete-note endpoint
        method: "POST",
        body: JSON.stringify({
            noteId: noteId
        }),
    }).then((_res) => {
        window.location.href = "/"; // reload window
    })
}