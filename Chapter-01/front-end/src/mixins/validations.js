export default {
  data() {
    return {
      rules: {
        required: value => !!value || "Required.",
        number: value => !isNaN(value) || "Invalid Number.",
        min: v => v.length >= 8 || "Min 8 characters",
        password: [
          v => !!v || "Password required",
          v =>
            /[a-z]/.test(v) ||
            "Password must contain at least one small letter.",
          v =>
            /[A-Z]/.test(v) ||
            "Password must contain at least one capital letter.",
          v => /[0-9]/.test(v) || "Password must contain at least one number.",
          v =>
            /[$&+,:;=?@#|'<>.^*()%!-]/.test(v) ||
            "Password must contain at least one special character.",

          v => v.length > 8 || "Password must not be less than 8 characters"
        ],
        username: [
          v => !!v || "Username required",
          v => !/[ ]/.test(v) || "Username can not have spaces."
        ],
        email: [
          v => !!v || "Email required",
          v =>
            /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
              v
            ) || "Invalid Email Address."
        ],
        firstName: [
          v => !!v || "First Name is required",
          v => !/[ ]/.test(v) || "First Name can not have spaces."
        ],
        lastName: [
          v => !!v || "Last Name is required",
          v => !/[ ]/.test(v) || "Last Name can not have spaces."
        ],
        gender: [v => !!v || "Gender is required"],
        dob: [v => !!v || "Date of Birth is required"],
        name: [v => !!v || "Name required"],
        grade: [
          v => !!v || "Required",
          v => v >= 0 || "Should be greater than zero.",
          v => v <= 100 || "Should be less than 100."
        ],
        optionalGrade: [
          v => !!v || "Required",
          v => v >= 0 || "Should be greater than zero.",
          v => v <= 100 || "Should be less than 100."
        ],
        weight: [
          v => !!v || "Required",
          v => v > 0 || "Should be greater than zero.",
          v => v <= 9 || "Should be less than 9."
        ],
        address: [
          v => !!v || "Address required",
          v => v.length <= 41 || "Address name too long",
          v =>
            /^[\u0080-\uFFFFa-zA-Z0-9\-.,'#*@\\/& ]+$/.test(v.trim()) ||
            "Address name can not contain special characters."
        ]
      }
    };
  }
};