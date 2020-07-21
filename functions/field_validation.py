# ******************************************************
# Functions for Field validation
# ******************************************************



def create_new_infield(nx, ny, nz,field_name):
    """
    Creates a new 3D infield that is saved as .npy file and can be used for validation purposes.

    Parameters
    ----------
    nx : field size in x-Direction.
    ny : field size in y-Direction.
    nz : field size in z-Direction.
    field_name : string of formatted field

    Returns
    -------
    testfield : New In_Field used for stencil computation

    """
    testfield = np.random.rand(nx, ny, nz)
    np.save("testfields/{}_infield.npy".format(field_name), testfield)

    return testfield


def create_val_infield(nx, ny, nz,field_name):
    """
    Loads an 3D infield that is saved as .npy file and can be used for validation purposes.
    Controls if new fieldsize is equivalent to the original field size.

    Parameters
    ----------
    nx : field size in x-Direction.
    ny : field size in y-Direction.
    nz : field size in z-Direction.

    Returns
    -------
    testfield : Field used for stencil computation

    """
    if os.path.exists("testfields/{}_infield.npy".format(field_name))== False :
        print("ERROR: Fieldname does not exist yet.")
        exit()
    
    testfield = np.load("testfields/{}_infield.npy".format(field_name))
    if (
        (testfield.shape[0] != nx)
        or (testfield.shape[1] != ny)
        or (testfield.shape[0] != nx)
    ):
        print("ERROR: New Infield has a different shape than the validation field.")
        exit()

    return testfield


def save_newoutfield(out_field,field_name):
    """
    Saves a new Out field to a .npy file.

    Parameters
    ----------
    out_field : 3D field after stencil computation
    field_name : field name

    Returns
    -------
    Print and save to .npy file

    """
    np.save("testfields/{}_outfield.npy".format(field_name), out_field)
    print("New output field {} saved.".format(field_name))


def validate_outfield(out_field,field_name):
    """
    Reads in the original file and compares it to the current out-field. Validates the results of the stencil computation

    Parameters
    ----------
    out_field : 3D field after stencil computation
    field_name : field name

    Returns
    -------
    valid_var : boolean variable if Validation of array is true/false

    """
    if os.path.exists("testfields/{}_outfield.npy".format(field_name))== False :
        print("ERROR: Fieldname does not exist yet.")
        exit()
    
    testfield = np.load("testfields/{}_outfield.npy".format(field_name))

    valid_var = np.all(np.equal(testfield, out_field))
    print("Result of field validation is:", valid_var)

    return valid_var
