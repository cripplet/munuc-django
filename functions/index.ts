import * as functions from 'firebase-functions'
import * as admin from 'firebase-admin'

admin.initializeApp();

export addMessage = functions.https.onRequest((req, res) => {
  const original = req.query.text;
  return functions.firestore.collection('users').document('lovelace').push({
      original: original
  }).then((snapshot) => {
      return res.redirect(303, snapshot.ref.toString());
  });
});
